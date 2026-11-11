# Capstone trials — before

Produced by `capstone_eval.py`.

```json
{
  "label": "before",
  "when": "2026-11-10T21:57:01",
  "trials": [
    {
      "trial": 1,
      "a_b": {
        "sent": 20,
        "logged": 20,
        "complete": 20,
        "records_with_a_null_required_field": 1,
        "status_codes": [
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          400,
          400,
          400,
          400,
          400
        ]
      },
      "c": {
        "under_8s": 8,
        "of": 10,
        "times": [
          [
            0.49,
            500
          ],
          [
            5.91,
            200
          ],
          [
            6.49,
            200
          ],
          [
            6.54,
            200
          ],
          [
            6.52,
            200
          ],
          [
            1.06,
            200
          ],
          [
            5.15,
            200
          ],
          [
            2.5,
            200
          ],
          [
            6.29,
            200
          ],
          [
            19.86,
            200
          ]
        ]
      },
      "failures": [
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota', 'status': 'RESOURCE_EXHAUSTED'}}"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "{'error'",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'Quota exceeded for metric generate_content_free_tier_requests', 'status': 'RESOURCE_EXHAUSTED'}}"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "{'error'",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. rate limit exceeded"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "503",
          "status": 500,
          "body": {
            "error": "Exception: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand.', 'status': 'UNAVAILABLE'}}"
          },
          "leak_markers_found": [
            "Exception",
            "UNAVAILABLE",
            "{'error'"
          ],
          "logged": true
        },
        {
          "simulated": "503",
          "status": 500,
          "body": {
            "error": "Exception: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The service is overloaded.', 'status': 'UNAVAILABLE'}}"
          },
          "leak_markers_found": [
            "Exception",
            "UNAVAILABLE",
            "{'error'"
          ],
          "logged": true
        }
      ]
    },
    {
      "trial": 2,
      "a_b": {
        "sent": 20,
        "logged": 20,
        "complete": 20,
        "records_with_a_null_required_field": 1,
        "status_codes": [
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          400,
          400,
          400,
          400,
          400
        ]
      },
      "c": {
        "under_8s": 8,
        "of": 10,
        "times": [
          [
            0.93,
            200
          ],
          [
            5.45,
            200
          ],
          [
            5.77,
            200
          ],
          [
            5.21,
            200
          ],
          [
            5.73,
            200
          ],
          [
            0.46,
            500
          ],
          [
            6.81,
            200
          ],
          [
            5.1,
            200
          ],
          [
            5.5,
            200
          ],
          [
            19.19,
            200
          ]
        ]
      },
      "failures": [
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota', 'status': 'RESOURCE_EXHAUSTED'}}"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "{'error'",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'Quota exceeded for metric generate_content_free_tier_requests', 'status': 'RESOURCE_EXHAUSTED'}}"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "{'error'",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. rate limit exceeded"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "503",
          "status": 500,
          "body": {
            "error": "Exception: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand.', 'status': 'UNAVAILABLE'}}"
          },
          "leak_markers_found": [
            "Exception",
            "UNAVAILABLE",
            "{'error'"
          ],
          "logged": true
        },
        {
          "simulated": "503",
          "status": 500,
          "body": {
            "error": "Exception: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The service is overloaded.', 'status': 'UNAVAILABLE'}}"
          },
          "leak_markers_found": [
            "Exception",
            "UNAVAILABLE",
            "{'error'"
          ],
          "logged": true
        }
      ]
    },
    {
      "trial": 3,
      "a_b": {
        "sent": 20,
        "logged": 20,
        "complete": 20,
        "records_with_a_null_required_field": 1,
        "status_codes": [
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          500,
          200,
          200,
          200,
          200,
          200,
          400,
          400,
          400,
          400,
          400
        ]
      },
      "c": {
        "under_8s": 8,
        "of": 10,
        "times": [
          [
            5.03,
            200
          ],
          [
            6.88,
            200
          ],
          [
            4.19,
            200
          ],
          [
            11.36,
            200
          ],
          [
            6.44,
            200
          ],
          [
            7.2,
            200
          ],
          [
            3.45,
            200
          ],
          [
            5.32,
            200
          ],
          [
            4.95,
            200
          ],
          [
            9.84,
            200
          ]
        ]
      },
      "failures": [
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota', 'status': 'RESOURCE_EXHAUSTED'}}"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "{'error'",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'Quota exceeded for metric generate_content_free_tier_requests', 'status': 'RESOURCE_EXHAUSTED'}}"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "{'error'",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "429",
          "status": 500,
          "body": {
            "error": "RuntimeError: Still rate limited after 4 attempts. Wait a minute and try again — your key is fine.\nLast error: 429 RESOURCE_EXHAUSTED. rate limit exceeded"
          },
          "leak_markers_found": [
            "RuntimeError",
            "Error:",
            "RESOURCE_EXHAUSTED",
            "Last error"
          ],
          "logged": true
        },
        {
          "simulated": "503",
          "status": 500,
          "body": {
            "error": "Exception: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand.', 'status': 'UNAVAILABLE'}}"
          },
          "leak_markers_found": [
            "Exception",
            "UNAVAILABLE",
            "{'error'"
          ],
          "logged": true
        },
        {
          "simulated": "503",
          "status": 500,
          "body": {
            "error": "Exception: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The service is overloaded.', 'status': 'UNAVAILABLE'}}"
          },
          "leak_markers_found": [
            "Exception",
            "UNAVAILABLE",
            "{'error'"
          ],
          "logged": true
        }
      ]
    }
  ]
}
```
