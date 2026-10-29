package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  An assessment objective of SP 800-171A: one determination statement that an assessor checks, tied to the requirement or to one item of its statement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171AssessmentObjective  {

  private String requirementObjectiveId;
  private String requirementDetermination;
  private String assessedRequirementItem;

}