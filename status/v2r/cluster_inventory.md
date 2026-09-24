# V2R cluster inventory

2026-09-24T14:50:36.323820+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324049563648 available bytes; 81.92% used; 112481459 free inodes.

server1 `/home`: 324049563648 available bytes; 81.92% used; 112481459 free inodes.

server1 `/tmp`: 324049563648 available bytes; 81.92% used; 112481459 free inodes.

server1 `/var/tmp`: 324049563648 available bytes; 81.92% used; 112481459 free inodes.

server1 `/mnt/raid5`: 416847540224 available bytes; 98.09% used; 337665815 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57437327360 available bytes; 96.80% used; 110427893 free inodes.

server2 `/home`: 57437327360 available bytes; 96.80% used; 110427893 free inodes.

server2 `/tmp`: 57437327360 available bytes; 96.80% used; 110427893 free inodes.

server2 `/var/tmp`: 57437327360 available bytes; 96.80% used; 110427893 free inodes.

server2 `/mnt/raid5`: 503887593472 available bytes; 96.52% used; 445167215 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84871335936 available bytes; 95.26% used; 114184521 free inodes.

server3 `/home`: 84871335936 available bytes; 95.26% used; 114184521 free inodes.

server3 `/data`: 160673050624 available bytes; 97.78% used; 225807733 free inodes.

server3 `/tmp`: 84871335936 available bytes; 95.26% used; 114184521 free inodes.

server3 `/var/tmp`: 84871335936 available bytes; 95.26% used; 114184521 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105749655552 available bytes; 94.10% used; 114348673 free inodes.

server4 `/home`: 105749655552 available bytes; 94.10% used; 114348673 free inodes.

server4 `/data`: 69166735360 available bytes; 99.04% used; 225256983 free inodes.

server4 `/tmp`: 105749655552 available bytes; 94.10% used; 114348673 free inodes.

server4 `/var/tmp`: 105749655552 available bytes; 94.10% used; 114348673 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
