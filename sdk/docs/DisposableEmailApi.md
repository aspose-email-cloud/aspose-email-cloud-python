# AsposeEmailCloudSdk.DisposableEmailApi (EmailCloud.disposable_email)

Checks if an email is a disposable one

<a name="is_disposable"></a>
## is_disposable

Description: Check email address is disposable             

Returns: true if address is disposable

Method call example:
```python
result = api.disposable_email.is_disposable(request)
```

### Parameter: request

Description: is_disposable method request.

See parameter model documentation at [DisposableEmailIsDisposableRequest](DisposableEmailIsDisposableRequest.md).

<details>
    <summary>Parameter initialization example:</summary>
    
```python
request = models.DisposableEmailIsDisposableRequest(
    address='example@mailcatch.com')
```

</details>

### Result

Description: true if address is disposable

Return type: [**ValueTOfBoolean**](ValueTOfBoolean.md)

<details>
    <summary>Result example</summary>

```python
result = 
```
</details>

### Complete example

<details>
    <summary>Method call example:</summary>

```python
api = EmailCloud(client_secret, client_id)

// Prepare parameters:
request = models.DisposableEmailIsDisposableRequest(
    address='example@mailcatch.com')

// Call method:
result = api.disposable_email.is_disposable(request)

// Result example:
result = 
```

</details>

[[Back to top]](#) [[Back to Model list]](Models.md) [[Back to README]](README.md)

