# V2R cluster inventory

2026-09-26T12:27:07.391207+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318178623488 available bytes; 82.25% used; 112474777 free inodes.

server1 `/home`: 318178623488 available bytes; 82.25% used; 112474777 free inodes.

server1 `/tmp`: 318178623488 available bytes; 82.25% used; 112474777 free inodes.

server1 `/var/tmp`: 318178623488 available bytes; 82.25% used; 112474777 free inodes.

server1 `/mnt/raid5`: 218558480384 available bytes; 99.00% used; 337537791 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19779059712 available bytes; 98.90% used; 110383260 free inodes.

server2 `/home`: 19779059712 available bytes; 98.90% used; 110383260 free inodes.

server2 `/tmp`: 19779059712 available bytes; 98.90% used; 110383260 free inodes.

server2 `/var/tmp`: 19779059712 available bytes; 98.90% used; 110383260 free inodes.

server2 `/mnt/raid5`: 239863767040 available bytes; 98.34% used; 444980230 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 82652614656 available bytes; 95.39% used; 114110841 free inodes.

server3 `/home`: 82652614656 available bytes; 95.39% used; 114110841 free inodes.

server3 `/data`: 123415490560 available bytes; 98.29% used; 225823801 free inodes.

server3 `/tmp`: 82652614656 available bytes; 95.39% used; 114110841 free inodes.

server3 `/var/tmp`: 82652614656 available bytes; 95.39% used; 114110841 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899810816 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899810816 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88558833664 available bytes; 98.78% used; 224878833 free inodes.

server4 `/tmp`: 105899810816 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899810816 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
