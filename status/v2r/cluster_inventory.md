# V2R cluster inventory

2026-09-26T09:30:07.104224+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318626988032 available bytes; 82.22% used; 112475099 free inodes.

server1 `/home`: 318626988032 available bytes; 82.22% used; 112475099 free inodes.

server1 `/tmp`: 318626988032 available bytes; 82.22% used; 112475099 free inodes.

server1 `/var/tmp`: 318626988032 available bytes; 82.22% used; 112475099 free inodes.

server1 `/mnt/raid5`: 218971176960 available bytes; 99.00% used; 337538658 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22320873472 available bytes; 98.75% used; 110403910 free inodes.

server2 `/home`: 22320873472 available bytes; 98.75% used; 110403910 free inodes.

server2 `/tmp`: 22320873472 available bytes; 98.75% used; 110403910 free inodes.

server2 `/var/tmp`: 22320873472 available bytes; 98.75% used; 110403910 free inodes.

server2 `/mnt/raid5`: 254199275520 available bytes; 98.24% used; 445022799 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661621760 available bytes; 95.39% used; 114110805 free inodes.

server3 `/home`: 82661621760 available bytes; 95.39% used; 114110805 free inodes.

server3 `/data`: 123656667136 available bytes; 98.29% used; 225827841 free inodes.

server3 `/tmp`: 82661621760 available bytes; 95.39% used; 114110805 free inodes.

server3 `/var/tmp`: 82661621760 available bytes; 95.39% used; 114110805 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105969508352 available bytes; 94.09% used; 114348080 free inodes.

server4 `/home`: 105969508352 available bytes; 94.09% used; 114348080 free inodes.

server4 `/data`: 89299787776 available bytes; 98.77% used; 224882738 free inodes.

server4 `/tmp`: 105969508352 available bytes; 94.09% used; 114348080 free inodes.

server4 `/var/tmp`: 105969508352 available bytes; 94.09% used; 114348080 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
