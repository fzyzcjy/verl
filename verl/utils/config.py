# Copyright 2024 Bytedance Ltd. and/or its affiliates
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

from typing import Dict

from omegaconf import DictConfig


def update_dict_with_config(dictionary: Dict, config: DictConfig):
    for key in dictionary:
        if hasattr(config, key):
            dictionary[key] = getattr(config, key)


def config_normalize_batch_size(config, key: str, divider: int):
    value_raw = config[key]
    assert value_raw % divider == 0
    value_normalized = value_raw // divider

    config.__delattr__(key)
    config[f'{key}_raw'] = value_raw
    config[f'{key}_normalized'] = value_normalized
