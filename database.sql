-- ─────────────────────────────────────────────
--  EPS CitaMédica — Esquema de Base de Datos
--  Compatible con MySQL (local) y Aiven (cloud)
-- ─────────────────────────────────────────────

CREATE DATABASE IF NOT EXISTS eps_citas
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE eps_citas;

-- ── Tabla de Pacientes ────────────────────────
CREATE TABLE IF NOT EXISTS pacientes (
    documento   VARCHAR(20)  NOT NULL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    apellido    VARCHAR(100) NOT NULL,
    telefono    VARCHAR(20),
    correo      VARCHAR(120),
    eps         VARCHAR(100),
    creado_en   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ── Tabla de Citas ────────────────────────────
CREATE TABLE IF NOT EXISTS citas (
    id          INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    documento   VARCHAR(20)  NOT NULL,
    medico      VARCHAR(100) NOT NULL,
    tipo_cita   VARCHAR(50)  NOT NULL,
    fecha       DATE         NOT NULL,
    hora        TIME         NOT NULL,
    direccion   VARCHAR(200),
    creado_en   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_citas_paciente
        FOREIGN KEY (documento) REFERENCES pacientes(documento)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
