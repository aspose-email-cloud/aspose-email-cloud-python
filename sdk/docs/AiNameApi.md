# AsposeEmailCloudSdk.AiNameApi

<a name="ai_name_complete"></a>
# **ai_name_complete**
> ai_name_complete(self, ai_name_complete_request)

The call proposes k most probable names for given starting characters.             

### Return type

[**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_complete(
    cakePrefix_ai_name_complete_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to complete. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_complete_async"></a>
# **ai_name_complete_async**
> ai_name_complete_async(self, ai_name_complete_request)

The call proposes k most probable names for given starting characters.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_complete_async(request).get() returns [**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_complete_async(
    cakePrefix_ai_name_complete_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to complete. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand"></a>
# **ai_name_expand**
> ai_name_expand(self, ai_name_expand_request)

Expands a person's name into a list of possible alternatives using options for expanding instructions.             

### Return type

[**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_expand(
    cakePrefix_ai_name_expand_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to expand. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand_async"></a>
# **ai_name_expand_async**
> ai_name_expand_async(self, ai_name_expand_request)

Expands a person's name into a list of possible alternatives using options for expanding instructions.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_expand_async(request).get() returns [**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_expand_async(
    cakePrefix_ai_name_expand_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to expand. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand_parsed"></a>
# **ai_name_expand_parsed**
> ai_name_expand_parsed(self, ai_name_expand_parsed_request)

Expands a person's parsed name into a list of possible alternatives using options for expanding instructions.             

### Return type

[**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_expand_parsed(
    cakePrefix_ai_name_expand_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedRequest**](AiNameParsedRequest.md)| Parsed name with options. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_expand_parsed_async"></a>
# **ai_name_expand_parsed_async**
> ai_name_expand_parsed_async(self, ai_name_expand_parsed_request)

Expands a person's parsed name into a list of possible alternatives using options for expanding instructions.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_expand_parsed_async(request).get() returns [**AiNameWeightedVariants**](AiNameWeightedVariants.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_expand_parsed_async(
    cakePrefix_ai_name_expand_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedRequest**](AiNameParsedRequest.md)| Parsed name with options. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format"></a>
# **ai_name_format**
> ai_name_format(self, ai_name_format_request)

Formats a person's name in correct case and name order using options for formatting instructions.             

### Return type

[**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    format=format, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_format(
    cakePrefix_ai_name_format_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        format=format, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to format. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **format** | **str**| Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (&#x3D; &#39;%t%F%m%N%L%p&#39;)     /format/FN+LN/ (&#x3D; &#39;%F%L&#39;)     /format/title+FN+LN/ (&#x3D; &#39;%t%F%L&#39;)     /format/FN+MN+LN/ (&#x3D; &#39;%F%M%N%L&#39;)     /format/title+FN+MN+LN/ (&#x3D; &#39;%t%F%M%N%L&#39;)     /format/FN+MI+LN/ (&#x3D; &#39;%F%m%N%L&#39;)     /format/title+FN+MI+LN/ (&#x3D; &#39;%t%F%m%N%L&#39;)     /format/LN/ (&#x3D; &#39;%L&#39;)     /format/title+LN/ (&#x3D; &#39;%t%L&#39;)     /format/LN+FN+MN/ (&#x3D; &#39;%L,%F%M%N&#39;)     /format/LN+title+FN+MN/ (&#x3D; &#39;%L,%t%F%M%N&#39;)     /format/LN+FN+MI/ (&#x3D; &#39;%L,%F%m%N&#39;)     /format/LN+title+FN+MI/ (&#x3D; &#39;%L,%t%F%m%N&#39;)  Custom format string - custom combination of characters and the next term placeholders:      &#39;%t&#39; - Title (prefix)     &#39;%F&#39; - First name     &#39;%f&#39; - First initial     &#39;%M&#39; - Middle name(s)     &#39;%m&#39; - Middle initial(s)     &#39;%N&#39; - Nickname     &#39;%L&#39; - Last name     &#39;%l&#39; - Last initial     &#39;%p&#39; - Postfix  If no value for format option was provided, its default value is &#39;%t%F%m%N%L%p&#39;              | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format_async"></a>
# **ai_name_format_async**
> ai_name_format_async(self, ai_name_format_request)

Formats a person's name in correct case and name order using options for formatting instructions.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_format_async(request).get() returns [**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    format=format, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_format_async(
    cakePrefix_ai_name_format_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        format=format, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to format. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **format** | **str**| Format of the name. Predefined format can be used by ID, or custom format can be specified. Predefined formats:      /format/default/ (&#x3D; &#39;%t%F%m%N%L%p&#39;)     /format/FN+LN/ (&#x3D; &#39;%F%L&#39;)     /format/title+FN+LN/ (&#x3D; &#39;%t%F%L&#39;)     /format/FN+MN+LN/ (&#x3D; &#39;%F%M%N%L&#39;)     /format/title+FN+MN+LN/ (&#x3D; &#39;%t%F%M%N%L&#39;)     /format/FN+MI+LN/ (&#x3D; &#39;%F%m%N%L&#39;)     /format/title+FN+MI+LN/ (&#x3D; &#39;%t%F%m%N%L&#39;)     /format/LN/ (&#x3D; &#39;%L&#39;)     /format/title+LN/ (&#x3D; &#39;%t%L&#39;)     /format/LN+FN+MN/ (&#x3D; &#39;%L,%F%M%N&#39;)     /format/LN+title+FN+MN/ (&#x3D; &#39;%L,%t%F%M%N&#39;)     /format/LN+FN+MI/ (&#x3D; &#39;%L,%F%m%N&#39;)     /format/LN+title+FN+MI/ (&#x3D; &#39;%L,%t%F%m%N&#39;)  Custom format string - custom combination of characters and the next term placeholders:      &#39;%t&#39; - Title (prefix)     &#39;%F&#39; - First name     &#39;%f&#39; - First initial     &#39;%M&#39; - Middle name(s)     &#39;%m&#39; - Middle initial(s)     &#39;%N&#39; - Nickname     &#39;%L&#39; - Last name     &#39;%l&#39; - Last initial     &#39;%p&#39; - Postfix  If no value for format option was provided, its default value is &#39;%t%F%m%N%L%p&#39;              | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format_parsed"></a>
# **ai_name_format_parsed**
> ai_name_format_parsed(self, ai_name_format_parsed_request)

Formats a person's parsed name in correct case and name order using options for formatting instructions.             

### Return type

[**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_format_parsed(
    cakePrefix_ai_name_format_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedRequest**](AiNameParsedRequest.md)| Parsed name with options. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_format_parsed_async"></a>
# **ai_name_format_parsed_async**
> ai_name_format_parsed_async(self, ai_name_format_parsed_request)

Formats a person's parsed name in correct case and name order using options for formatting instructions.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_format_parsed_async(request).get() returns [**AiNameFormatted**](AiNameFormatted.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_format_parsed_async(
    cakePrefix_ai_name_format_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedRequest**](AiNameParsedRequest.md)| Parsed name with options. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize"></a>
# **ai_name_genderize**
> ai_name_genderize(self, ai_name_genderize_request)

Detect person's gender from name string.             

### Return type

[**AiNameGenderHypothesisList**](AiNameGenderHypothesisList.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_genderize(
    cakePrefix_ai_name_genderize_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to genderize. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize_async"></a>
# **ai_name_genderize_async**
> ai_name_genderize_async(self, ai_name_genderize_request)

Detect person's gender from name string.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_genderize_async(request).get() returns [**AiNameGenderHypothesisList**](AiNameGenderHypothesisList.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_genderize_async(
    cakePrefix_ai_name_genderize_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to genderize. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize_parsed"></a>
# **ai_name_genderize_parsed**
> ai_name_genderize_parsed(self, ai_name_genderize_parsed_request)

Detect person's gender from parsed name.             

### Return type

[**AiNameGenderHypothesisList**](AiNameGenderHypothesisList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_genderize_parsed(
    cakePrefix_ai_name_genderize_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedRequest**](AiNameParsedRequest.md)| Gender detection request data. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_genderize_parsed_async"></a>
# **ai_name_genderize_parsed_async**
> ai_name_genderize_parsed_async(self, ai_name_genderize_parsed_request)

Detect person's gender from parsed name.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_genderize_parsed_async(request).get() returns [**AiNameGenderHypothesisList**](AiNameGenderHypothesisList.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_genderize_parsed_async(
    cakePrefix_ai_name_genderize_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedRequest**](AiNameParsedRequest.md)| Gender detection request data. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match"></a>
# **ai_name_match**
> ai_name_match(self, ai_name_match_request)

Compare people's names. Uses options for comparing instructions.             

### Return type

[**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    name, 
    other_name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_match(
    cakePrefix_ai_name_match_request_cakeCodePostProcessor(
        name, 
        other_name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to match. | 
 **other_name** | **str**| Another name to match. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match_async"></a>
# **ai_name_match_async**
> ai_name_match_async(self, ai_name_match_request)

Compare people's names. Uses options for comparing instructions.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_match_async(request).get() returns [**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    name, 
    other_name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_match_async(
    cakePrefix_ai_name_match_request_cakeCodePostProcessor(
        name, 
        other_name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to match. | 
 **other_name** | **str**| Another name to match. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match_parsed"></a>
# **ai_name_match_parsed**
> ai_name_match_parsed(self, ai_name_match_parsed_request)

Compare people's parsed names and attributes. Uses options for comparing instructions.             

### Return type

[**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_match_parsed(
    cakePrefix_ai_name_match_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedMatchRequest**](AiNameParsedMatchRequest.md)| Parsed names to match. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_match_parsed_async"></a>
# **ai_name_match_parsed_async**
> ai_name_match_parsed_async(self, ai_name_match_parsed_request)

Compare people's parsed names and attributes. Uses options for comparing instructions.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_match_parsed_async(request).get() returns [**AiNameMatchResult**](AiNameMatchResult.md)

### Request Parameters
```python
__init__(self, 
    request)
```

### Usage
```python
AiNameApi.ai_name_match_parsed_async(
    cakePrefix_ai_name_match_parsed_request_cakeCodePostProcessor(
        request))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AiNameParsedMatchRequest**](AiNameParsedMatchRequest.md)| Parsed names to match. | 

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse"></a>
# **ai_name_parse**
> ai_name_parse(self, ai_name_parse_request)

Parse name to components.             

### Return type

[**AiNameComponentList**](AiNameComponentList.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_parse(
    cakePrefix_ai_name_parse_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to parse. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse_async"></a>
# **ai_name_parse_async**
> ai_name_parse_async(self, ai_name_parse_request)

Parse name to components.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_parse_async(request).get() returns [**AiNameComponentList**](AiNameComponentList.md)

### Request Parameters
```python
__init__(self, 
    name, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_parse_async(
    cakePrefix_ai_name_parse_request_cakeCodePostProcessor(
        name, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A name to parse. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse_email_address"></a>
# **ai_name_parse_email_address**
> ai_name_parse_email_address(self, ai_name_parse_email_address_request)

Parse person's name out of an email address.             

### Return type

[**AiNameExtractedList**](AiNameExtractedList.md)

### Request Parameters
```python
__init__(self, 
    email_address, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_parse_email_address(
    cakePrefix_ai_name_parse_email_address_request_cakeCodePostProcessor(
        email_address, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Email address to parse. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

<a name="ai_name_parse_email_address_async"></a>
# **ai_name_parse_email_address_async**
> ai_name_parse_email_address_async(self, ai_name_parse_email_address_request)

Parse person's name out of an email address.             

Performs operation asynchronously.

### Return type

Returns multiprocessing.pool.AsyncResult.
ai_name_parse_email_address_async(request).get() returns [**AiNameExtractedList**](AiNameExtractedList.md)

### Request Parameters
```python
__init__(self, 
    email_address, 
    language=language, 
    location=location, 
    encoding=encoding, 
    script=script, 
    style=style)
```

### Usage
```python
AiNameApi.ai_name_parse_email_address_async(
    cakePrefix_ai_name_parse_email_address_request_cakeCodePostProcessor(
        email_address, 
        language=language, 
        location=location, 
        encoding=encoding, 
        script=script, 
        style=style))
```


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Email address to parse. | 
 **language** | **str**| An ISO-639 code of the language; either 639-1 or 639-3 (e.g. \&quot;it\&quot; or \&quot;ita\&quot; for Italian).              | [optional] [default to ]
 **location** | **str**| A geographic code such as an ISO-3166 two letter country code, for example \&quot;FR\&quot; for France.              | [optional] [default to ]
 **encoding** | **str**| A character encoding name. | [optional] [default to ]
 **script** | **str**| A writing system code; starts with the ISO-15924 script name. | [optional] [default to ]
 **style** | **str**| Name writing style. Enum, available values: Formal, Informal, Legal, Academic | [optional] [default to 0]

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

