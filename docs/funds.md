# Funds

The `Funds` class from `gtr.services.funds` gives access to the GTR-2 Funds endpoint. This can be imported directly from the `gtr` module.

```python
>>> from gtr import Funds
```

To access the GTR-V2 data, create a Funds object:

```python
>>> funds = Funds()
```

## Funds Methods

There are two methods assosciated with the Funds class.

### fund

Searches for a fund by id:

```python
>>> results = funds.fund("Fund ID")
```

All of the methods in the funds class return a `requests.Response` object, which has a `json()` method giving access to the returned data as Python objects.

```python
>>> results.json()
{'id': '246FE7FB-4116-4B1B-8C13-8BB728256AE1', 'valuePounds': {'amount': 310869, 'currencyCode': 'GBP'}, 'href': 'http://gtr.rcuk.ac.uk:80/gtr/api/funds/246FE7FB-4116-4B1B-8C13-8BB728256AE1', 'category': 'INCOME_ACTUAL', 'start': 1288569600000, 'created': 1453777286000, 'end': 1383177600000, 'links': {'link': [{'href': 'http://gtr.rcuk.ac.uk:80/gtr/api/organisations/2512EF1C-401B-4222-9869-A770D4C5FAC7', 'rel': 'FUNDER', 'otherAttributes': {}, 'start': 1288569600000, 'end': 1383177600000}, {'href': 'http://gtr.rcuk.ac.uk:80/gtr/api/projects/4DE350EC-21F2-4C45-9E8B-459A13C277E3', 'rel': 'FUNDED', 'otherAttributes': {}, 'start': 1288569600000, 'end': 1383177600000}]}}
```


### funds

Searches for funds by the following fields:

  - title
  - amount
  - organisation name
  - type

```python
>>> results = funds.Funds("search term", field=search_field)
>>> results.json()
>>> {'page': 1, 'totalPages': 622, 'size': 20...}
```