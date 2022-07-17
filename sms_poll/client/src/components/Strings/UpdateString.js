import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Button,
  Input,
  FormControl,
  useDisclosure,
  IconButton,
} from "@chakra-ui/react"
import { Fragment, useState } from "react"
import React from "react"
import { FiEdit } from "react-icons/fi"

function UpdateString({ string, updateString }) {
  const { isOpen, onOpen, onClose } = useDisclosure()
  const [updatedName, setUpdatedName] = useState("")
  const initialRef = React.useRef()
  const { name, value } = string

  return (
    <Fragment>
      <IconButton icon={<FiEdit />} isRound="true" onClick={onOpen} />
      <Modal
        isCentered
        initialFocusRef={initialRef}
        isOpen={isOpen}
        onClose={onClose}
      >
        <ModalOverlay />
        <ModalContent w="90%">
          <ModalHeader>{`Edit string "${name}"`}</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl>
              <Input
                ref={initialRef}
                placeholder={`New string for "${name}"`}
                defaultValue={value}
                onChange={(e) => setUpdatedName(e.target.value)}
                onFocus={(e) => setUpdatedName(e.target.value)}
              />
            </FormControl>
          </ModalBody>

          <ModalFooter>
            <Button mr={3} onClick={onClose}>
              Cancel
            </Button>
            <Button
              colorScheme="blue"
              onClick={() => updateString(name, updatedName, onClose)}
            >
              Submit
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Fragment>
  )
}

export default UpdateString
