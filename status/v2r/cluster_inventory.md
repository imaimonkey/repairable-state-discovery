# V2R cluster inventory

2026-09-25T12:59:07.452515+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319110000640 available bytes; 82.20% used; 112477578 free inodes.

server1 `/home`: 319110000640 available bytes; 82.20% used; 112477578 free inodes.

server1 `/tmp`: 319110000640 available bytes; 82.20% used; 112477578 free inodes.

server1 `/var/tmp`: 319110000640 available bytes; 82.20% used; 112477578 free inodes.

server1 `/mnt/raid5`: 366597476352 available bytes; 98.32% used; 337547945 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8304435200 available bytes; 99.54% used; 110408779 free inodes.

server2 `/home`: 8304435200 available bytes; 99.54% used; 110408779 free inodes.

server2 `/tmp`: 8304435200 available bytes; 99.54% used; 110408779 free inodes.

server2 `/var/tmp`: 8304435200 available bytes; 99.54% used; 110408779 free inodes.

server2 `/mnt/raid5`: 324364029952 available bytes; 97.76% used; 445077840 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84210237440 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84210237440 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142275133440 available bytes; 98.03% used; 225810722 free inodes.

server3 `/tmp`: 84210237440 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84210237440 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665224704 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665224704 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232001327104 available bytes; 96.79% used; 224960289 free inodes.

server4 `/tmp`: 105665224704 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665224704 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
