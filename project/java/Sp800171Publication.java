package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  One revision of SP 800-171 as a whole: its requirement families, each holding its security requirements, with the assessment procedures of the matching revision of SP 800-171A inside each requirement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171Publication  {

  private String sp800171Revision;
  private List<Sp800171Family> requirementFamilies;

}