import pandas as pd
from googleapiclient.discovery import Resource


def required_scopes() -> list:
    return ['https://www.googleapis.com/auth/spreadsheets']


def write_to_spreadsheet(service: Resource, spreadsheet_id: str, spreadsheet_range: str, df: pd.DataFrame, **kwargs) -> dict:
    value_input_option = kwargs.get('value_input_option', 'USER_ENTERED')
    values = df.fillna('').values.tolist()
    if kwargs.get('header', True):
        values.insert(0, df.columns.values.tolist())

    body = {
        'valueInputOption': value_input_option,
        'data': [
            {
                'range': spreadsheet_range,
                'values': values,
            },
        ],
    }
    return service.spreadsheets() \
        .values() \
        .batchUpdate(spreadsheetId=spreadsheet_id, body=body) \
        .execute()
