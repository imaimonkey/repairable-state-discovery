# V2R cluster inventory

2026-09-26T09:14:51.722635+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318736416768 available bytes; 82.22% used; 112475795 free inodes.

server1 `/home`: 318736416768 available bytes; 82.22% used; 112475795 free inodes.

server1 `/tmp`: 318736416768 available bytes; 82.22% used; 112475795 free inodes.

server1 `/var/tmp`: 318736416768 available bytes; 82.22% used; 112475795 free inodes.

server1 `/mnt/raid5`: 218999959552 available bytes; 99.00% used; 337538715 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22326587392 available bytes; 98.75% used; 110403911 free inodes.

server2 `/home`: 22326587392 available bytes; 98.75% used; 110403911 free inodes.

server2 `/tmp`: 22326587392 available bytes; 98.75% used; 110403911 free inodes.

server2 `/var/tmp`: 22326587392 available bytes; 98.75% used; 110403911 free inodes.

server2 `/mnt/raid5`: 254642647040 available bytes; 98.24% used; 445023289 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661711872 available bytes; 95.39% used; 114110815 free inodes.

server3 `/home`: 82661711872 available bytes; 95.39% used; 114110815 free inodes.

server3 `/data`: 123661807616 available bytes; 98.29% used; 225828076 free inodes.

server3 `/tmp`: 82661711872 available bytes; 95.39% used; 114110815 free inodes.

server3 `/var/tmp`: 82661711872 available bytes; 95.39% used; 114110815 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106046001152 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106046001152 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89328656384 available bytes; 98.77% used; 224883323 free inodes.

server4 `/tmp`: 106046001152 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106046001152 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
