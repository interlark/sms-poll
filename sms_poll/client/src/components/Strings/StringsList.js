import { HStack, StackDivider, Text, VStack } from "@chakra-ui/react"
import UpdateString from "./UpdateString"

function StringsList({ strings, updateString }) {
  return (
    <VStack
      divider={<StackDivider />}
      borderColor="gray.100"
      borderWidth="2px"
      p="5"
      mt="4"
      borderRadius="lg"
      w="100%"
      alignItems="stretch"
    >
      {strings.map(string => (
        <HStack key={string.name}>
          <Text w="100%" p="8px" borderRadius="lg">
            {string.value}
          </Text>
          <UpdateString string={string} updateString={updateString} />
        </HStack>
      ))}
    </VStack>
  )
}

export default StringsList
