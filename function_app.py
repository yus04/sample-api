import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="microsoft_teams")
def microsoft_teams(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = {
        "title": "Teams を使用してリモートワーカーをサポートする",
        "description": "設定のガイダンス、短いビデオ、およびヒントを使用して、リモート作業のために、Teams を管理する方法を説明します。",
        "content": {
            "value1": "Teams は組織に対して有効になっています",
            "value2": "新しい Teams ユーザーのセットアップは状態を確認する",
            "value3": "ゲストアクセスは許可されています"
        },
    }
    
    return func.HttpResponse(
        body=json.dumps(data),
        status_code=200,
        mimetype="application/json"
    )


@app.route(route="user_management")
def user_management(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = {
        "title": "ユーザーの管理",
        "description": "ユーザーアカウントの追加、編集、削除とパスワードのリセットを行います。"
    }
    
    return func.HttpResponse(
        body=json.dumps(data),
        status_code=200,
        mimetype="application/json"
    )


@app.route(route="invoice")
def invoice(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = {
        "title": "請求",
        "description": "￥0"
    }
    
    return func.HttpResponse(
        body=json.dumps(data),
        status_code=200,
        mimetype="application/json"
    )


@app.route(route="training_guide")
def training_guide(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = {
        "title": "トレーニングとガイド",
        "content": {
            "item1": {
                "item-title": "管理者向けのトレーニング",
                "item-description": "Microsoft 365 のチュートリアルとビデオ"
            },
            "item2": {
                "item-title": "カスタマイズされたセットアップガイド",
                "item-description": "組織に適したセットアップパスの選択"
            },
            "item3": {
                "item-title": "ユーザー向けのトレーニング",
                "item-description": "Microsoft 365 と Office アプリの使用方法について説明します。"
            }
        },
    }
    
    return func.HttpResponse(
        body=json.dumps(data),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="office_app")
def office_app(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = {
        "title": "Office アプリ",
        "description": "Office デスクトップアプリをインストール"
    }
    
    return func.HttpResponse(
        body=json.dumps(data),
        status_code=200,
        mimetype="application/json"
    )
