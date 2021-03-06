opt = {'task': 'twitter',
       'history_size':-1,
       'download_path': 'ParlAI/downloads',
       'datatype': 'train',
       'image_mode': 'raw',
       'numthreads': 1,
       'hide_labels': False,
       'batchsize': 32,
       'batch_sort': True,
       'context_length': -1,
       'include_labels': True,
       'datapath': 'ParlAI/data',
       'model': 'legacy:seq2seq:0',
       'model_file': 'original_ParlAI_twitter_seq2seq_model/twitter_seq2seq_model',
       'dict_class': 'parlai.core.dict:DictionaryAgent',
       'evaltask': None,
       'display_examples': False,
       'num_epochs': -1,
       'max_train_time': 205200.0,
       'validation_every_n_secs': 600.0,
       'save_every_n_secs': -1,
       'save_after_valid': True,
       'validation_max_exs': -1,
       'validation_patience': 18,
       'validation_metric': 'ppl',
       'validation_metric_mode': 'min',
       'validation_cutoff': 1.0,
       'dict_build_first': True,
       'load_from_checkpoint': True,
       'tensorboard_log': False,
       'tensorboard_tag': None,
       'tensorboard_metrics': None,
       'tensorboard_comment': '',
       'dict_maxexs': -1,
       'dict_include_valid': False,
       'dict_include_test': False,
       'log_every_n_secs': 15.0,
       'image_size': 256,
       'image_cropsize': 224,
       'init_model': None,
       'hiddensize': 1024,
       'embeddingsize': 300,
       'numlayers': 3, 'learningrate': 1.0,
       'dropout': 0.0,
       'gradient_clip': 0.1,
       'bidirectional': False, 'attention': 'none',
       'attention_length': 48, 'attention_time': 'post',
       'no_cuda': True, 'gpu': -1,
       'rank_candidates': False, 'truncate': 30,
       'rnn_class': 'lstm', 'decoder': 'same',
       'lookuptable': 'enc_dec', 'optimizer': 'sgd',
       'momentum': 0.9, 'embedding_type': 'glove',
       'numsoftmax': 1, 'report_freq': 0.001,
       'history_replies': 'label_else_model',
       'person_tokens': False,
       'dict_file': '/checkpoint/ahm/20180615/twit_s2s/soft=1_hs=1024_esz=300_att=none_nl=3_rnn=lstm_lr=1_dr=0.1_clip=0.1_lt=encdec_opt=sgd_emb=glove_tr=150/model.dict',
       'dict_initpath': None,
       'dict_language': 'english',
       'dict_max_ngram_size': -1, 'dict_minfreq': 0,
       'dict_maxtokens': 30000, 'dict_nulltoken': '__NULL__',
       'dict_starttoken': '__START__', 'dict_endtoken': '__END__',
       'dict_unktoken': '__UNK__', 'dict_tokenizer': 're', 'dict_lower': True,
       'parlai_home': 'ParlAI',
       'override': {'task': 'twitter', 'max_train_time': '205200', 'model': 'seq2seq', 'numsoftmax': '1', 'hiddensize': '1024', 'embeddingsize': '300', 'attention': 'none', 'numlayers': '3', 'rnn_class': 'lstm', 'learningrate': '1',
                    'dropout': '0.0',
                    'gradient_clip': '0.1', 'lookuptable': 'enc_dec', 'optimizer': 'sgd', 'embedding_type': 'glove', 'momentum': '0.9', 'batchsize': '32', 'batch_sort': 'True', 'truncate': '30', 'validation_every_n_secs': '600', 'validation_metric': 'ppl', 'validation_metric_mode': 'min', 'validation_patience': '18', 'save_after_valid': 'True', 'load_from_checkpoint': 'True', 'dict_lower': 'True', 'dict_maxtokens': '30000', 'log_every_n_secs': '15', 'model_file': ''},
       'starttime': 'Jun15_16-53', 'show_advanced_args': False,
       'pytorch_teacher_task': None, 'pytorch_teacher_dataset': None,
       'pytorch_datapath': None, 'numworkers': 4, 'pytorch_preprocess': False,
       'pytorch_teacher_batch_sort': False, 'batch_sort_cache_type': 'pop',
       'batch_length_range': 5, 'shuffle': False, 'batch_sort_field': 'text',
       'pytorch_context_length': -1, 'pytorch_include_labels': True, 'num_examples': -1,
       'metrics': 'all', 'beam_size': 1, 'beam_log_freq': 0.0, 'topk': 1,
       'softmax_layer_bias': False, 'bpe_debug': False, 'dict_textfields': 'text,labels'}