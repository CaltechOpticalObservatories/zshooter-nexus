# ZShooter & WMKO ToO Concept Views

Views included:
- `views/too_architecture.d2`
- `views/program_submission.d2`
- `views/alert_response_loop.d2`
- `views/too_completion_loop.d2`

Render:

```bash
mkdir -p out
for f in views/*.d2; do
  d2 --layout elk "$f" "out/$(basename "${f%.d2}").svg"
done
```