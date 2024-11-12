"""Borro tabla Tipo

Revision ID: fb017342376b
Revises: d86eab640b99
Create Date: 2024-11-08 16:52:28.475030

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fb017342376b'
down_revision = 'd86eab640b99'
branch_labels = None
depends_on = None


def upgrade():
    # Eliminar la restricción de la clave foránea
    op.drop_constraint('equipo_ibfk_6', 'equipo', type_='foreignkey')
    
    # Ahora puedes eliminar la tabla Tipo
    op.drop_table('tipo')

def downgrade():
    # Volver a crear la tabla Tipo si es necesario
    op.create_table(
        'tipo',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Agregar la restricción de la clave foránea nuevamente
    op.create_foreign_key(
        'equipo_ibfk_6', 'equipo', 'tipo', ['tipo_id'], ['id']
    )
