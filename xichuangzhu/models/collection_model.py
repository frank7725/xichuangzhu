#-*- coding: UTF-8 -*-

from flask import g

class Collection:

# GET

	# get an author's all collections
	@staticmethod
	def get_collections_by_author(authorID):
		query = "SELECT * FROM collection WHERE AuthorID = %d" % authorID
		g.cursor.execute(query)
		return g.cursor.fetchall()

	# get single collection
	@staticmethod
	def get_collection(collectionID):
		query = '''SELECT collection.CollectionID, collection.Collection, collection.Introduction, author.AuthorID, author.Author, author.Abbr AS AuthorAbbr, dynasty.Dynasty, dynasty.Abbr AS DynastyAbbr\n
			FROM collection, author, dynasty\n
			WHERE collection.AuthorID = author.AuthorID\n
			AND author.DynastyID = dynasty.dynastyID
			AND collectionID = %d''' % collectionID
		g.cursor.execute(query)
		return g.cursor.fetchone()

# NEW

	# add a collection
	@staticmethod
	def add_collection(collection, authorID, introduction):
		query = '''INSERT INTO collection (Collection, AuthorID, Introduction) VALUES\n
			('%s', %d, '%s')''' % (collection, authorID, introduction)
		g.cursor.execute(query)
		g.conn.commit()
		return g.cursor.lastrowid

# EDIT

	# edit a collection
	@staticmethod
	def edit_collection(collection, authorID, introduction, collectionID):
		query = '''UPDATE collection SET Collection = '%s', AuthorID = %d, Introduction = '%s'\n
			WHERE CollectionID = %d''' % (collection, authorID, introduction, collectionID)
		g.cursor.execute(query)
		return g.conn.commit()