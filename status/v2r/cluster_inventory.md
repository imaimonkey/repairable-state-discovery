# V2R cluster inventory

2026-09-26T11:01:40.437813+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318213943296 available bytes; 82.25% used; 112474833 free inodes.

server1 `/home`: 318213943296 available bytes; 82.25% used; 112474833 free inodes.

server1 `/tmp`: 318213943296 available bytes; 82.25% used; 112474833 free inodes.

server1 `/var/tmp`: 318213943296 available bytes; 82.25% used; 112474833 free inodes.

server1 `/mnt/raid5`: 218761539584 available bytes; 99.00% used; 337538217 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19850518528 available bytes; 98.89% used; 110384897 free inodes.

server2 `/home`: 19850518528 available bytes; 98.89% used; 110384897 free inodes.

server2 `/tmp`: 19850518528 available bytes; 98.89% used; 110384897 free inodes.

server2 `/var/tmp`: 19850518528 available bytes; 98.89% used; 110384897 free inodes.

server2 `/mnt/raid5`: 242284466176 available bytes; 98.33% used; 444979308 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662080512 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82662080512 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123566825472 available bytes; 98.29% used; 225825996 free inodes.

server3 `/tmp`: 82662080512 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82662080512 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926602752 available bytes; 94.09% used; 114347961 free inodes.

server4 `/home`: 105926602752 available bytes; 94.09% used; 114347961 free inodes.

server4 `/data`: 88890195968 available bytes; 98.77% used; 224880540 free inodes.

server4 `/tmp`: 105926602752 available bytes; 94.09% used; 114347961 free inodes.

server4 `/var/tmp`: 105926602752 available bytes; 94.09% used; 114347961 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
