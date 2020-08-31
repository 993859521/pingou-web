# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class Louceng(db.Model):
    __tablename__ = 'louceng'

    id = db.Column(db.Integer, primary_key=True)
    tieziid = db.Column(db.Integer, nullable=False)
    Context = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    owner = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
