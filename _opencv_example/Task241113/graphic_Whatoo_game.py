import cv2
import numpy as np
import random
from PIL import Image

class Whatoo:
    def __init__(self, img):
        # 카드 이미지를 읽어오고 48장으로 분할
        self.deck = []
        self.load_cards(img)
        
    def load_cards(self, img):
        # 이미지 크기를 정확히 맞춤 (1188x1337으로 고정)        
        img_width = img.shape[0]
        img_height = img.shape[1]
        print(img_width, img_height)        

        img = cv2.resize(img, (1188, 1337))  # 이미지 크기를 1188x1337로 고정       
                
        card_height = img_height // 8
        card_width = img_width // 6  # 각 카드의 크기: 167x198
                
        print(card_width, card_height)            
        
        for col in range(8):
            for row in range(6):
                # 각 카드를 분할하여 정확한 크기로 deck에 추가
                card = img[row * card_width: (row + 1) * card_width,
                           col * card_height: (col + 1) * card_height]
                
                # 모든 카드를 정확히 167x198 크기로 조정
                #card = cv2.resize(card, (card_width, card_height))
                self.deck.append(card)                
        print("Length: ", self.deck.__len__())
                
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def deal_cards(self):
        players = [[] for _ in range(4)]
        for i in range(4):
            players[i] = self.deck[i * 7:(i + 1) * 7]
        return players

    def display_player_cards(self, players):
        # 모든 카드가 동일한 크기인지 확인하고 배경 크기 설정
        card_height, card_width = players[0][0].shape[:2]  # 모든 카드가 167x198인지 확인
        background_height = card_height * 4 + 300  # 4명의 플레이어, 세로 여백 포함
        background_width = card_width * 7 + 300    # 각 플레이어당 7장의 카드, 가로 여백 포함
        
        # 배경을 정확히 계산된 크기로 설정
        background = np.zeros((background_height, background_width, 3), dtype=np.uint8)
        print("background : ",background_height, background_width)
        background[:] = (34, 139, 34)  # 녹색 배경 설정 (RGB 색상)

        x_min = 200
        y_min = 100
        for i, player_cards in enumerate(players):
            for j, card in enumerate(player_cards):                
                y_offset = i * (card_height + 5)                    
                x_offset = j * (card_width + 5)                
                background[y_min + y_offset : y_min + y_offset + card_height, x_min + x_offset : x_min + x_offset + card_width] = card
            self.write_userName(50, (i+1) * (card_height + 5), f"Player{i+1}", background)
        cv2.imshow("Game Result", background) 
        
        # 현재 폴더에 이미지 저장
        self.save_image(background)
               
    def write_userName(self, posX, posY, playerName, background):
        # 텍스트 설정
        text = playerName
        position = (posX, posY)  # 텍스트 위치 (x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX  # 폰트 설정
        font_scale = 1  # 폰트 크기 (크기 10에 맞도록 크기 조정 필요)
        color = (255, 255, 255)  # 흰색 텍스트 (BGR 형식)
        thickness = 2  # 텍스트 두께

        # 이미지에 텍스트 추가
        cv2.putText(background, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        
    def run_game(self):
        self.shuffle_deck()
        players = self.deal_cards()
        self.display_player_cards(players)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self, result_image):
        import os
        
        # 현재 코드가 존재하는 폴더 경로
        current_folder = os.path.dirname(os.path.abspath(__file__))

        # 저장 경로 설정
        output_path = os.path.join(current_folder, 'output.png')

        # 이미지 확장자 추출
        extension = os.path.splitext(output_path)[1]

        # 이미지 인코딩
        result, encoded_img = cv2.imencode(extension, result_image)

        if result:
            with open(output_path, mode='w+b') as f:
                encoded_img.tofile(f)
            print(f"이미지가 {output_path}에 저장되었습니다.")
        else:
            print("이미지 인코딩에 실패했습니다.")
            
# 한글 경로를 Pillow로 읽기
card_image_path = "c:/Users/aloho/문서/Github/openCV-SeoultechMSD/_opencv_example/00_d/Flower_cards.png"
img_pil = Image.open(card_image_path)

# Pillow 이미지를 OpenCV 형식으로 변환
img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# 게임 실행
game = Whatoo(img)
game.run_game()
