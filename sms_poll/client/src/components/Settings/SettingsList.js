import {
  Button,
  Checkbox,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
  useDisclosure,
  VStack,
  ModalOverlay,
} from "@chakra-ui/react"
import React from "react"

function SettingsList({ deleteVotes, flags, toggleFlag }) {
  const { isOpen, onOpen, onClose } = useDisclosure()
  const getFlagValue = name => flags.find(flag => flag.name === name).value
  const checkboxStyle = () => {
    return (
      {
        sx: {
          "& .chakra-checkbox__label": {
            marginInlineStart: "0.8rem",
          },
        }
      })
  }

  return (
    <VStack>
      <VStack p="5" alignItems="stretch">
        <Checkbox
          defaultChecked={getFlagValue("distinct_poll")}
          onChange={() => toggleFlag("distinct_poll")}
          {...checkboxStyle()}
        >
          Allow only one vote from one sender
        </Checkbox>

        <Checkbox
          defaultChecked={getFlagValue("light_theme_poll")}
          pt={5} pb={5}
          onChange={() => toggleFlag("light_theme_poll")}
          {...checkboxStyle()}
        >
          Use light theme
        </Checkbox>

        <Button
          colorScheme="gray"
          px="8"
          h="45"
          color="gray.500"
          pl="10" pr="10"
          onClick={onOpen}
        >
          Clear votes
        </Button>
      </VStack>

      <Modal isCentered isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent w="90%">
          <ModalHeader>Clear all votes</ModalHeader>
          <ModalBody>
            Are you sure you want to delete all recieved votes?
          </ModalBody>
          <ModalFooter>
            <Button mr={3} onClick={onClose}>
              Cancel
            </Button>
            <Button colorScheme="red" onClick={() => deleteVotes(onClose)}>
              Delete
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </VStack>
  )
}

export default SettingsList
