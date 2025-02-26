
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R', 'F', 'F', 'T', 'T', 'T']
moves_dir = {'N':'R', 'S':'R', 'E':'F', 'W':'F'}


@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    #data = request.json()
    logger.info(request.json)
    #data = request.json
    #move_dir = get_can_move_list(data['arena']['state'])
    return moves[random.randrange(len(moves))] 

def get_can_move_list(move_json):
    can_move_list = []
    for each_url in move_json:
        if move_json[each_url]['wasHit'] == True:
            can_move_list.append(move_dir(move_json[each_url]['direction']))
    if len(can_move_list)!=0:
        return random.choice(can_move_list)
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
