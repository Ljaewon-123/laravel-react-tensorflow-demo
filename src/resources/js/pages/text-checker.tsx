import { TextareaWithButton } from "@/components/textarea-with-button"
import { useState } from "react"

export default function MessagePage() {
  const [message, setMessage] = useState("")
  const [submitted, setSubmitted] = useState(false)

  const handleChange = (value: string) => {
    setSubmitted(message)
  }

  return (
    <div className="min-h-screen flex flex-col items-center">
      {/* 위쪽 여백을 조정하여 "중앙보다 약간 위" 느낌 */}
      <div className="mt-24 w-full max-w-md px-4">
        <TextareaWithButton
          value={message}
          onChange={setMessage}
          onSubmit={handleChange}
        />
        
        {submitted && (
          <div className="mt-6 p-4 rounded-lg border bg-muted/30">
            <p className="font-semibold">입력한 내용:</p>
            <p className="text-sm text-muted-foreground">{submitted}</p>
          </div>
        )}
      </div>
    </div>
  )
}
