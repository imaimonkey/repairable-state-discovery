# V2R cluster inventory

2026-09-24T07:20:15.095914+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324450373632 available bytes; 81.90% used; 112491237 free inodes.

server1 `/home`: 324450373632 available bytes; 81.90% used; 112491237 free inodes.

server1 `/tmp`: 324450373632 available bytes; 81.90% used; 112491237 free inodes.

server1 `/var/tmp`: 324450373632 available bytes; 81.90% used; 112491237 free inodes.

server1 `/mnt/raid5`: 517417750528 available bytes; 97.63% used; 337722819 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57852481536 available bytes; 96.77% used; 110431127 free inodes.

server2 `/home`: 57852481536 available bytes; 96.77% used; 110431127 free inodes.

server2 `/tmp`: 57852481536 available bytes; 96.77% used; 110431127 free inodes.

server2 `/var/tmp`: 57852481536 available bytes; 96.77% used; 110431127 free inodes.

server2 `/mnt/raid5`: 518576140288 available bytes; 96.42% used; 445181145 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127188078592 available bytes; 92.90% used; 114199250 free inodes.

server3 `/home`: 127188078592 available bytes; 92.90% used; 114199250 free inodes.

server3 `/data`: 139064872960 available bytes; 98.08% used; 225834328 free inodes.

server3 `/tmp`: 127188078592 available bytes; 92.90% used; 114199250 free inodes.

server3 `/var/tmp`: 127188078592 available bytes; 92.90% used; 114199250 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105789591552 available bytes; 94.10% used; 114349198 free inodes.

server4 `/home`: 105789591552 available bytes; 94.10% used; 114349198 free inodes.

server4 `/data`: 289780977664 available bytes; 96.00% used; 225367037 free inodes.

server4 `/tmp`: 105789591552 available bytes; 94.10% used; 114349198 free inodes.

server4 `/var/tmp`: 105789591552 available bytes; 94.10% used; 114349198 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
