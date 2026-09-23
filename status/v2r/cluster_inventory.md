# V2R cluster inventory

2026-09-23T23:33:18.039797+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325645582336 available bytes; 81.83% used; 112501461 free inodes.

server1 `/home`: 325645582336 available bytes; 81.83% used; 112501461 free inodes.

server1 `/tmp`: 325645582336 available bytes; 81.83% used; 112501461 free inodes.

server1 `/var/tmp`: 325645582336 available bytes; 81.83% used; 112501461 free inodes.

server1 `/mnt/raid5`: 1367408701440 available bytes; 93.73% used; 337736318 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41034919936 available bytes; 97.71% used; 110432556 free inodes.

server2 `/home`: 41034919936 available bytes; 97.71% used; 110432556 free inodes.

server2 `/tmp`: 41034919936 available bytes; 97.71% used; 110432556 free inodes.

server2 `/var/tmp`: 41034919936 available bytes; 97.71% used; 110432556 free inodes.

server2 `/mnt/raid5`: 534385934336 available bytes; 96.31% used; 445205497 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292861136896 available bytes; 83.66% used; 114213558 free inodes.

server3 `/home`: 292861136896 available bytes; 83.66% used; 114213558 free inodes.

server3 `/data`: 82306842624 available bytes; 98.86% used; 225845723 free inodes.

server3 `/tmp`: 292861136896 available bytes; 83.66% used; 114213558 free inodes.

server3 `/var/tmp`: 292861136896 available bytes; 83.66% used; 114213558 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106213453824 available bytes; 94.07% used; 114352239 free inodes.

server4 `/home`: 106213453824 available bytes; 94.07% used; 114352239 free inodes.

server4 `/data`: 293061533696 available bytes; 95.95% used; 225422971 free inodes.

server4 `/tmp`: 106213453824 available bytes; 94.07% used; 114352239 free inodes.

server4 `/var/tmp`: 106213453824 available bytes; 94.07% used; 114352239 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
