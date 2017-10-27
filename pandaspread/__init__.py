import pandas as pd
from googleapiclient.discovery import Resource


def write_to_spreadsheet(service: Resource, spreadsheet_id: str, spreadsheet_range: str, df: pd.DataFrame, **kwargs):
    value_input_option = kwargs.get('value_input_option', 'USER_ENTERED')
    values = [df.columns.values.tolist()] + df.fillna('').values.tolist()
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
