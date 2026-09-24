# V2R cluster inventory

2026-09-24T06:30:26.710887+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324508962816 available bytes; 81.90% used; 112491671 free inodes.

server1 `/home`: 324508962816 available bytes; 81.90% used; 112491671 free inodes.

server1 `/tmp`: 324508962816 available bytes; 81.90% used; 112491671 free inodes.

server1 `/var/tmp`: 324508962816 available bytes; 81.90% used; 112491671 free inodes.

server1 `/mnt/raid5`: 517573701632 available bytes; 97.63% used; 337723769 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57882427392 available bytes; 96.77% used; 110431205 free inodes.

server2 `/home`: 57882427392 available bytes; 96.77% used; 110431205 free inodes.

server2 `/tmp`: 57882427392 available bytes; 96.77% used; 110431205 free inodes.

server2 `/var/tmp`: 57882427392 available bytes; 96.77% used; 110431205 free inodes.

server2 `/mnt/raid5`: 520226549760 available bytes; 96.41% used; 445191906 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127200329728 available bytes; 92.90% used; 114197456 free inodes.

server3 `/home`: 127200329728 available bytes; 92.90% used; 114197456 free inodes.

server3 `/data`: 140512477184 available bytes; 98.06% used; 225835747 free inodes.

server3 `/tmp`: 127200329728 available bytes; 92.90% used; 114197456 free inodes.

server3 `/var/tmp`: 127200329728 available bytes; 92.90% used; 114197456 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805467648 available bytes; 94.10% used; 114349278 free inodes.

server4 `/home`: 105805467648 available bytes; 94.10% used; 114349278 free inodes.

server4 `/data`: 328176623616 available bytes; 95.46% used; 225372955 free inodes.

server4 `/tmp`: 105805467648 available bytes; 94.10% used; 114349278 free inodes.

server4 `/var/tmp`: 105805467648 available bytes; 94.10% used; 114349278 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
