# V2R cluster inventory

2026-09-24T07:15:34.697046+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324452667392 available bytes; 81.90% used; 112491276 free inodes.

server1 `/home`: 324452667392 available bytes; 81.90% used; 112491276 free inodes.

server1 `/tmp`: 324452667392 available bytes; 81.90% used; 112491276 free inodes.

server1 `/var/tmp`: 324452667392 available bytes; 81.90% used; 112491276 free inodes.

server1 `/mnt/raid5`: 517423230976 available bytes; 97.63% used; 337722818 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57852755968 available bytes; 96.77% used; 110431137 free inodes.

server2 `/home`: 57852755968 available bytes; 96.77% used; 110431137 free inodes.

server2 `/tmp`: 57852755968 available bytes; 96.77% used; 110431137 free inodes.

server2 `/var/tmp`: 57852755968 available bytes; 96.77% used; 110431137 free inodes.

server2 `/mnt/raid5`: 518723915776 available bytes; 96.42% used; 445181387 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127185686528 available bytes; 92.90% used; 114199540 free inodes.

server3 `/home`: 127185686528 available bytes; 92.90% used; 114199540 free inodes.

server3 `/data`: 139077423104 available bytes; 98.08% used; 225834432 free inodes.

server3 `/tmp`: 127185686528 available bytes; 92.90% used; 114199540 free inodes.

server3 `/var/tmp`: 127185686528 available bytes; 92.90% used; 114199540 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105789874176 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789874176 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 293067304960 available bytes; 95.95% used; 225367227 free inodes.

server4 `/tmp`: 105789874176 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789874176 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
