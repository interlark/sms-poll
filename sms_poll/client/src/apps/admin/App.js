import {
  Heading,
  IconButton,
  Spinner,
  Tab,
  TabList,
  TabPanel,
  TabPanels,
  Tabs,
  useColorMode,
  useToast,
  VStack,
} from "@chakra-ui/react"
import { useEffect, useState } from "react"
import { FaMoon, FaSun } from "react-icons/fa"
import AddItem from "../../components/Item/AddItem"
import ItemList from "../../components/Item/ItemList"
import SettingsList from "../../components/Settings/SettingsList"
import StringsList from "../../components/Strings/StringsList"
import PollInfo from "../../components/Poll/PollInfo"
import axios from "axios"


function App() {
  const initState = {
    flags: [
      {name: 'distinct_poll', value: true},
      {name: 'light_theme_poll', value: false},
    ],
    strings: [
      {name: '#', value: '#'},
      {name: 'Item', value: 'Item'},
      {name: 'Votes', value: 'Votes'},
      {name: 'Phone', value: '(123) 456-7890'},
    ],
    items: [],
    wifiIP: 'NO IP ADDRESS',
    title: 'List of items',
    loading: true,
  }
  const [state, setState] = useState(initState)
  const toast = useToast()

  const getFlags = async () => {
    const res = await axios.get('/settings/flags')
    return res.data
  }

  const getStrings = async () => {
    const res = await axios.get("/settings/strings")
    return res.data
  }

  const getItems = async () => {
    const res = await axios.get("/items/")
    return res.data
  }

  const getWifiIP = async () => {
    const res = await axios.get('/phone/wifi_ip')
    return res.data
  }

  useEffect(() => {
    const fetchData = async() => {
      try {
        const flags = await getFlags()
        const strings = await getStrings()
        const items = await getItems()
        const wifiIP = await getWifiIP()
        setState({...state, flags, strings, items, phone, wifiIP, loading: false})
      } catch (error) {
        setState({...state, loading: false})
        console.error(error)
        toast({
          title: "Error occured during load data!",
          position: "top",
          status: "error",
          duration: 2000,
          isClosable: true,
        })
      }
    }
    fetchData()
  }, [])

  const deleteItem = async (id) => {
    const res = await axios.delete(`/items/${id}`)
    setState({...state, items: state.items.filter(item => item.id !== id)})
  }

  const deleteItemsAll = async () => {
    const res = await axios.delete('/items/')
    setState({...state, items: []})
  }

  const updateItem = async (id, name, onClose) => {
    name = name.trim()
    if (!name) {
      toast({
        title: "Name can not be empty!",
        position: "top",
        status: "warning",
        duration: 2000,
        isClosable: true,
      })
      return
    }

    const res = await axios.put(`/items/${id}`, {name})
    const updatedItems = state.items.map(item => {
        if (item.id === id) {
          item.name = name
        }
        return item
    })

    setState({...state, items: updatedItems})
    onClose()
  }

  const addItem = async (name) => {
    const res = await axios.post('/items/', {name})
    setState({...state, items: [...state.items, {...res.data, votes_count: 0}]})
  }

  const updateString = async (name, value, onClose) => {
    value = value.trim()
    if (!value) {
      toast({
        title: "String can not be empty!",
        position: "top",
        status: "warning",
        duration: 2000,
        isClosable: true,
      })
      return
    }

    const res = await axios.put("/settings/strings", {name, value})
    const updatedStrings = state.strings.map(string => {
      if (string.name === name) {
        string.value = value
      }
      return string
    })

    setState({...state, strings: updatedStrings})
    onClose()
  }

  const deleteVotes = async (onClose) => {
    const res = await axios.delete("/votes/")
    toast({ title: "Votes deleted", duration: 2000, status: "success" })
    onClose()
  }

  const toggleFlag = async (name) => {
    console.log('NAME:', name)
    const flag = state.flags.find(flag => flag.name === name)
    console.log('FLAG:', flag)
    const value = !flag.value
    const res = await axios.put("/settings/flags", {name, value})
    const updatedFlags = state.flags.map(flag => {
      if (flag.name === name) {
        flag.value = value
      }
      return flag
    })
    setState({...state, flags: updatedFlags})
  }

  const updateWifiIP = async () => {
    const wifiIP = await getWifiIP()
    setState({...state, wifiIP: wifiIP})
  }

  const onTabChange = (tabIndex) => {
    const titles = ['List of items', 'App strings', 'App settings', 'Poll info']
    setState({...state, title: titles[tabIndex]})
  }

  const { colorMode, toggleColorMode } = useColorMode()
  const { loading, items, strings, flags, phone, wifiIP, title } = state

  if (loading) {
    return (
      <VStack minH="100vh" justifyContent="center">
        <Spinner size="xl" />
      </VStack>
    )
  }

  return (
    <VStack p={4} minH="100vh" pb={28}>
      <IconButton
        icon={colorMode === "light" ? <FaSun /> : <FaMoon />}
        isRound="true"
        size="md"
        alignSelf="flex-end"
        onClick={toggleColorMode}
      />

      <Heading p="5" fontWeight="extrabold" size="xl">
        {title}
      </Heading>
      <Tabs
        isFitted
        borderRadius="lg"
        w="100%"
        maxW={{ base: "90vw", sm: "80vw", lg: "60vw", xl: "40vw" }}
        onChange={onTabChange}
      >
        <TabList>
          <Tab>Items</Tab>
          <Tab>Strings</Tab>
          <Tab>Settings</Tab>
          <Tab>Info</Tab>
        </TabList>
        <TabPanels>
          <TabPanel>
            <VStack>
              <AddItem addItem={addItem} />
              <ItemList
                items={items}
                updateItem={updateItem}
                deleteItem={deleteItem}
                deleteItemsAll={deleteItemsAll}
              />
            </VStack>
          </TabPanel>
          <TabPanel>
            <StringsList strings={strings} updateString={updateString} />
          </TabPanel>
          <TabPanel>
            <SettingsList
              deleteVotes={deleteVotes}
              flags={flags}
              toggleFlag={toggleFlag}
            />
          </TabPanel>
          <TabPanel>
            <PollInfo
                wifiIP={wifiIP}
                updateWifiIP={updateWifiIP}
            />
          </TabPanel>
        </TabPanels>
      </Tabs>
    </VStack>
  )
}

export default App
