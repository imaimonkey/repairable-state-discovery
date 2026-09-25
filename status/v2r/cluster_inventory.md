# V2R cluster inventory

2026-09-25T08:03:46.614704+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318854746112 available bytes; 82.21% used; 112480366 free inodes.

server1 `/home`: 318854746112 available bytes; 82.21% used; 112480366 free inodes.

server1 `/tmp`: 318854746112 available bytes; 82.21% used; 112480366 free inodes.

server1 `/var/tmp`: 318854746112 available bytes; 82.21% used; 112480366 free inodes.

server1 `/mnt/raid5`: 386602455040 available bytes; 98.23% used; 337557896 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22843973632 available bytes; 98.73% used; 110410481 free inodes.

server2 `/home`: 22843973632 available bytes; 98.73% used; 110410481 free inodes.

server2 `/tmp`: 22843973632 available bytes; 98.73% used; 110410481 free inodes.

server2 `/var/tmp`: 22843973632 available bytes; 98.73% used; 110410481 free inodes.

server2 `/mnt/raid5`: 334085128192 available bytes; 97.69% used; 445095147 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84437118976 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84437118976 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142390665216 available bytes; 98.03% used; 225812135 free inodes.

server3 `/tmp`: 84437118976 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84437118976 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625440256 available bytes; 94.11% used; 114350335 free inodes.

server4 `/home`: 105625440256 available bytes; 94.11% used; 114350335 free inodes.

server4 `/data`: 249028493312 available bytes; 96.56% used; 225009277 free inodes.

server4 `/tmp`: 105625440256 available bytes; 94.11% used; 114350335 free inodes.

server4 `/var/tmp`: 105625440256 available bytes; 94.11% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
