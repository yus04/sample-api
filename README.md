# sample-api

## Microsoft Teams API
### 概要
このAPIは、Teamsを使用してリモートワーカーをサポートするための情報を提供します。

### リクエスト
- URL: /microsoft_teams
- Method: GET
- Query Parameters: なし

### レスポンス
```json
{
    "title": "Teams を使用してリモートワーカーをサポートする",
    "description": "設定のガイダンス、短いビデオ、およびヒントを使用して、リモート作業のために、Teams を管理する方法を説明します。",
    "content": {
        "value1": "Teams は組織に対して有効になっています",
        "value2": "新しい Teams ユーザーのセットアップは状態を確認する",
        "value3": "ゲストアクセスは許可されています"
    }
}
```

## User Management API

### 概要
このAPIは、ユーザーアカウントの追加、編集、削除、およびパスワードのリセットを行います。

### リクエスト
- URL: /user_management
- Method: GET
- Query Parameters: なし
- レスポンス

```json
{
    "title": "ユーザーの管理",
    "description": "ユーザーアカウントの追加、編集、削除とパスワードのリセットを行います。"
}
```

## Invoice API

### 概要
このAPIは、請求に関する情報を提供します。

### リクエスト
- URL: /invoice
- Method: GET
- Query Parameters: なし

### レスポンス
```json
{
    "title": "請求",
    "description": "￥0"
}
```

## Training Guide API

### 概要
このAPIは、トレーニングとガイドに関する情報を提供します。

### リクエスト
- URL: /training_guide
- Method: GET
- Query Parameters: なし

### レスポンス
```json
{
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
    }
}
```

## Office App API

### 概要
このAPIは、Officeデスクトップアプリをインストールするための情報を提供します。

### リクエスト
- URL: /office_app
- Method: GET
- Query Parameters: なし

### レスポンス
```json
{
    "title": "Office アプリ",
    "description": "Office デスクトップアプリをインストール"
}
```