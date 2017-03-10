# Scout

## Goal
> Be informed. Do not search. Scout will do it for you! Be informed about what you want to be informed.

In professional football manager has a lot of work. Too much to search for new players. Whenever he
wants to hire someone he sends scout. Then his mission begins. Unless appropriate candidate will not be found he keeps on searching.
When he finds potential player matching criteria he creates report.
You are the manager. You don't have time to search for data in the Internet or anywhere it can be retrieved. Let 
## Terms
**Scout** has to run when the **mission** is started. It should be as easy as following:
```python
    notes = self.__read_notes(mission)
    research_result = self.__do_research(mission, notes)
    self.__send_report_if_needed(mission, research_result)
    self.__update_notes(research_result)

```
Research is about following logic:
```python
    current_value = value_reader.read()
    match = criteria.test(current_value)
    if match.found:
        notification = notifier.verify(current_value, notes)
        if notification.should_notify:
            return ResearchResult.FOUND(current_value)
        else:
            return ResearchResult.FOUND_BUT_KEEP_SILENT(current_value)
    else:
        return ResearchResult.NOT_FOUND()
```
Before doing research it may be needed to read **notes**. 
When the mission is cyclical scout has to remember what he has found recently.
    
## Usecase
Exemplary use case for app may be:
- checking if price of some goods decreased
- waiting for perfect job offer
- notify about blog entries mentioning some topic
