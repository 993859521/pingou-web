# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class Tiezi(db.Model):
    __tablename__ = 'tiezi'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    images = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    context = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    owner = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, server_default=db.FetchedValue())
    lcnum = db.Column(db.Integer, server_default=db.FetchedValue())
