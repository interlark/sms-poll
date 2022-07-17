import { Button, HStack, Input, useToast } from "@chakra-ui/react"
import { useState } from "react"

function AddItem({ addItem }) {
  const toast = useToast()
  const [content, setContent] = useState("")
  const [statusInput, setStatusInput] = useState(true)

  function handleSubmit(e) {
    e.preventDefault()

    const name = content.trim()

    if (!name) {
      toast({
        title: "Name can not be empty!",
        position: "top",
        status: "warning",
        duration: 2000,
        isClosable: true,
      })
      setStatusInput(false)

      return setContent("")
    }

    addItem(name)
    setContent("")
  }

  if (content && !statusInput) {
    setStatusInput(true)
  }

  return (
    <form onSubmit={handleSubmit}>
      <HStack mt="4" mb="4">
        <Input
          h="46"
          borderColor={!statusInput ? "red.300" : "transparent"}
          variant="filled"
          placeholder="Item name"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          mr="2"
        />
        <Button colorScheme="blue" px="8" pl="10" pr="10" h="46" type="submit">
          Add
        </Button>
      </HStack>
    </form>
  )
}

export default AddItem
