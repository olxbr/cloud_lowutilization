main_config = {
    "api_listner_ip": "0.0.0.0",
    "api_listner_port": "8080",
    "api_flash_debug": True,

    "criteria_percent_max_cpu": 50,
    "criteria_max_mem_available_pct": 50,
    "criteria_network_io_mega": 150,  # 1GB
    "criteria_aggregation_value": 14,
    "criteria_aggegation_unit": 'days',

    "system_timezone": "UTC",
    "system_ssh_timeout": 4,
    "system_ntp_server": "0.north-america.pool.ntp.org, 1.north-america.pool.ntp.org, 2.north-america.pool.ntp.org, 3.north-america.pool.ntp.org",
    "system_loglevel": "DEBUG",
    "system_logfile": None,
    "system_test_mode_ids": [
        {'id': 'i-0aeb5dcc19892e8a6', 'region': 'us-east-1'},
        {'id': 'i-0f6cf1cb60ec1e35a', 'region': 'sa-east-1'},  # Não temos a chave mas é low utilization no report
        {'id': 'i-017546d384aea17d1', 'region': 'sa-east-1'},  # NGA - team infra e temos chave
        {'id': 'i-012b33752543a8680', 'region': 'sa-east-1'},  # Malta, temos chave
        {'id': 'i-07e5c2f095f72af6e', 'region': 'sa-east-1'},
        {'id': 'i-0349b84be2af801c4', 'region': 'sa-east-1'},
        {'id': 'i-0d13136d94c625a5e', 'region': 'sa-east-1'}
    ],
    "system_test_picke_file": "/Volumes/DataDisk/csmaniotto/projects/cloud_monitoring/df_test.pkl",

    # "aws_regions": ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1', 'ap-southeast-1','ap-southeast-2','ap-northeast-1'],
    "aws_regions": ['sa-east-1', 'us-east-1'],
    "aws_ssh_key_folder": "/Volumes/DataDisk/csmaniotto/projects/pemkeys/",
    "aws_tag_exclude": ['elasticbeanstalk:', 'aws:', 'k8s.'],

    # "mongo-server": "localhost:32768",
    "mongo-server": "abc833672e4d711e7996102ed2455e02-33316868.sa-east-1.elb.amazonaws.com:27017",
    "mongo_db-": "clound_mon",
    "mongo_collection": "low_utilization"
}

log_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - [%(levelname)s] %(name)s [%(module)s.%(funcName)s:%(lineno)d]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'info': {
            'format': '%(levelname)s:%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'debug': {
            'format': '%(asctime)s %(filename)-18s %(levelname)-8s: [ %(funcName)s():%(lineno)s]:  %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'debug',
        }
    },
    'loggers': {
        '__main__': {  # logging from this module will be logged in VERBOSE level
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },

        'aws_interface': {  # logging from this module will be logged in VERBOSE level
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },

        'tools': {  # logging from this module will be logged in VERBOSE level
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['default']
    },

}
