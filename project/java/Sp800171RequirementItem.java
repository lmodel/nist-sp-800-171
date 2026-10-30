package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One item of a requirement statement: a lettered item such as 03.01.01.a, or a numbered item under a lettered one such as 03.01.01.c.01.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171RequirementItem  {

  private String requirementItemId;
  private String requirementItemText;
  private List<Sp800171RequirementItem> requirementSubitems;


}