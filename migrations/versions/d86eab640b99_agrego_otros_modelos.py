"""Agrego otros modelos

Revision ID: d86eab640b99
Revises: fe6adc37b7d1
Create Date: 2024-11-05 19:12:26.647934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd86eab640b99'
down_revision = 'fe6adc37b7d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accesorio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo_accesorio', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fabricante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_fabricante', sa.String(length=50), nullable=False),
    sa.Column('pais_origen', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modelo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_proveedor', sa.String(length=50), nullable=False),
    sa.Column('contacto', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('anio_fabricacion', sa.Integer(), nullable=True),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.Column('modelo_id', sa.Integer(), nullable=False),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.Column('proveedor_id', sa.Integer(), nullable=False),
    sa.Column('fabricante_id', sa.Integer(), nullable=False),
    sa.Column('accesorio_id', sa.Integer(), nullable=False),
    sa.Column('tipo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['accesorio_id'], ['accesorio.id'], ),
    sa.ForeignKeyConstraint(['fabricante_id'], ['fabricante.id'], ),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.ForeignKeyConstraint(['modelo_id'], ['modelo.id'], ),
    sa.ForeignKeyConstraint(['proveedor_id'], ['proveedor.id'], ),
    sa.ForeignKeyConstraint(['tipo_id'], ['tipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipo')
    op.drop_table('proveedor')
    op.drop_table('modelo')
    op.drop_table('fabricante')
    op.drop_table('accesorio')
    # ### end Alembic commands ###
