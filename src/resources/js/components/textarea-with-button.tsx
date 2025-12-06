import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

interface Props {
  value: string
  onChange: (value: string) => void
  onSubmit: () => void
}

export function TextareaWithButton({ value, onChange, onSubmit }: Props) {
  return (
    <div className="grid w-full gap-2">
      <Textarea 
        placeholder="Type your message here."
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
      <Button onClick={onSubmit}>Send message</Button>
    </div>
  )
}
