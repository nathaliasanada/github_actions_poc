from flask import Flask, request, jsonify

app = Flask(_name_)

comments_by_content_id = {}

@app.route('/api/comment/new', methods=['POST'])
def new_comment():
    comment_data = request.get_json()
    email = comment_data['email']
    comment = comment_data['comment']
    content_id = comment_data['content_id']
    if content_id not in comments_by_content_id:
        comments_by_content_id[content_id] = []
    comments_by_content_id[content_id].append({'email': email, 'comment': comment})
    return jsonify({'success': True})

@app.route('/api/comment/list/<int:content_id>')
def list_comments(content_id):
    if content_id not in comments_by_content_id:
        return jsonify({'success': False, 'error': 'Content not found'})
    return jsonify({'success': True, 'comments': comments_by_content_id[content_id]})

if __name__ == '__main__':
    app.run()