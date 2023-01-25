import os

def save(email, result):
    path = './data/' + email + '/' + result['date']
    file = result['keyword'] + '.txt'
    os.makedirs(path, exist_ok=True)

    with open(path + '/' + file, 'a') as f:
        for piece in result['news']:
            f.write(piece['title'])
            f.write('\n')
            f.write(piece['media'])
            f.write('\n')
            f.write(piece['link'])
            f.write('\n\n')
            f.write(piece['contents'])
            f.write('\n\n ====================================== \n')
