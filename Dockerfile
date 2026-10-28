# ---- Build Stage: Maven 构建 ----
FROM maven:3.6.3-jdk-8 AS builder
WORKDIR /build
COPY settings.xml /root/.m2/settings.xml
COPY pom.xml .
COPY src ./src
RUN mvn package -DskipTests -B -q

# ---- Run Stage: 运行 jar ----
FROM openjdk:8u312-jdk-bullseye

# Used only to upgrade a mounted legacy payment template before Java starts.
RUN apt-get update \
  && apt-get install -y --no-install-recommends python3 \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /app \
  && mkdir /app/springboot \
  && mkdir /app/appsystems \
  && mkdir /app/applogs \
  && mkdir /app/appsystems/config \
  && mkdir /app/appsystems/qr \
  && mkdir /app/applogs/dump \
  && mkdir /app/appsystems/tmp

COPY src/main/resources/start.sh /app/start.sh
COPY scripts/upgrade_payment_template.py scripts/prepare_payment_template.sh /app/payment-template/
COPY src/main/resources/templates/payment.html /app/payment-template/payment.html
COPY --from=builder /build/target/*.jar /app/appsystems/

RUN chmod +x /app/start.sh

WORKDIR /app/appsystems

ENTRYPOINT ["/bin/sh", "-c","/app/start.sh"]
