from zope.interface import Interface

class IConversationView(Interface):
    def comments():
        """Return all comments in the conversation.
        """

    def conversation():
        """Return active conversation.
        """

    def root_comments():
        """Return all of the root comments for a conversation.
        """

    def children(comment):
        """Return all of the children comments for a parent comment.
        """
    
    def GetTimePost():
        """ Returm time of post"""    
        

class ICommentView(Interface):

    def comment():
        """Return active comment.
        """

    def author():
        """Return the name of the author of this comment.
        If no full name is known the userid is returned.
        """

    def quotedBody():
        """Return the body of the comment, quoted for a reply.
        """

    def get_prefs_user():
        ''' return myvindula view '''
