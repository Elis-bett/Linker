# LINKER
Simple app to turn long URLs into short for more convenient use.

___
## Functional Requirements
1. Get short link from long URL
2. Redirect from short link to the initial URL

## Quality Attributes
1. High availability (The server must be available at any time)
2. Short delay (Redirection must be fast)
3. Scalability (System must support large users number)

---
## Architecture Design
```
       _________       ______________       __________
      |         |     |              |     |          |
      | Client  |---->| Link Service |---->| Database |
      |_________|     |______________|     |__________|
                             |                  ^
                       ______v____              |
                      |           |             |
                      | Shortener |_____________|
                      |___________|
      
```

### To test FastAPI
```commandline
fastapi dev
```