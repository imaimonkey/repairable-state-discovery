# V2R cluster inventory

2026-09-24T07:40:26.135776+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324444631040 available bytes; 81.90% used; 112491044 free inodes.

server1 `/home`: 324444631040 available bytes; 81.90% used; 112491044 free inodes.

server1 `/tmp`: 324444631040 available bytes; 81.90% used; 112491044 free inodes.

server1 `/var/tmp`: 324444631040 available bytes; 81.90% used; 112491044 free inodes.

server1 `/mnt/raid5`: 516959281152 available bytes; 97.63% used; 337722775 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57839648768 available bytes; 96.77% used; 110431138 free inodes.

server2 `/home`: 57839648768 available bytes; 96.77% used; 110431138 free inodes.

server2 `/tmp`: 57839648768 available bytes; 96.77% used; 110431138 free inodes.

server2 `/var/tmp`: 57839648768 available bytes; 96.77% used; 110431138 free inodes.

server2 `/mnt/raid5`: 517943623680 available bytes; 96.42% used; 445180434 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127154909184 available bytes; 92.90% used; 114199815 free inodes.

server3 `/home`: 127154909184 available bytes; 92.90% used; 114199815 free inodes.

server3 `/data`: 138714009600 available bytes; 98.08% used; 225833515 free inodes.

server3 `/tmp`: 127154909184 available bytes; 92.90% used; 114199815 free inodes.

server3 `/var/tmp`: 127154909184 available bytes; 92.90% used; 114199815 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780289536 available bytes; 94.10% used; 114349181 free inodes.

server4 `/home`: 105780289536 available bytes; 94.10% used; 114349181 free inodes.

server4 `/data`: 285698830336 available bytes; 96.05% used; 225366786 free inodes.

server4 `/tmp`: 105780289536 available bytes; 94.10% used; 114349181 free inodes.

server4 `/var/tmp`: 105780289536 available bytes; 94.10% used; 114349181 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
