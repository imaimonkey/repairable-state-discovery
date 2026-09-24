# V2R cluster inventory

2026-09-24T04:46:56.361966+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324623740928 available bytes; 81.89% used; 112492826 free inodes.

server1 `/home`: 324623740928 available bytes; 81.89% used; 112492826 free inodes.

server1 `/tmp`: 324623740928 available bytes; 81.89% used; 112492826 free inodes.

server1 `/var/tmp`: 324623740928 available bytes; 81.89% used; 112492826 free inodes.

server1 `/mnt/raid5`: 455574515712 available bytes; 97.91% used; 337724622 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40768946176 available bytes; 97.73% used; 110430466 free inodes.

server2 `/home`: 40768946176 available bytes; 97.73% used; 110430466 free inodes.

server2 `/tmp`: 40768946176 available bytes; 97.73% used; 110430466 free inodes.

server2 `/var/tmp`: 40768946176 available bytes; 97.73% used; 110430466 free inodes.

server2 `/mnt/raid5`: 524004646912 available bytes; 96.38% used; 445195399 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292400197632 available bytes; 83.68% used; 114200211 free inodes.

server3 `/home`: 292400197632 available bytes; 83.68% used; 114200211 free inodes.

server3 `/data`: 24358907904 available bytes; 99.66% used; 225840627 free inodes.

server3 `/tmp`: 292400197632 available bytes; 83.68% used; 114200211 free inodes.

server3 `/var/tmp`: 292400197632 available bytes; 83.68% used; 114200211 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105836126208 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105836126208 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 253377167360 available bytes; 96.50% used; 225366841 free inodes.

server4 `/tmp`: 105836126208 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105836126208 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
