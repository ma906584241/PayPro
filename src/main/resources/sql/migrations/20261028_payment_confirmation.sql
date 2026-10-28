-- EXISTING DATABASES ONLY. Apply once before deploying the new application.
-- Back up first. Do not rerun pay.sql: that file drops the order table.
-- NULL credentials intentionally keep existing rows on the legacy review flow.
ALTER TABLE t_order
    ADD COLUMN payment_confirm_token_hash CHAR(64) NULL DEFAULT NULL,
    ADD COLUMN payment_confirmed_at DATETIME NULL DEFAULT NULL,
    ADD COLUMN admin_notice_status VARCHAR(16) NULL DEFAULT NULL;
