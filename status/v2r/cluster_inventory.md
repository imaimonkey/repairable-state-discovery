# V2R cluster inventory

2026-09-26T11:13:52.850009+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318220955648 available bytes; 82.25% used; 112474826 free inodes.

server1 `/home`: 318220955648 available bytes; 82.25% used; 112474826 free inodes.

server1 `/tmp`: 318220955648 available bytes; 82.25% used; 112474826 free inodes.

server1 `/var/tmp`: 318220955648 available bytes; 82.25% used; 112474826 free inodes.

server1 `/mnt/raid5`: 218736840704 available bytes; 99.00% used; 337538164 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19851341824 available bytes; 98.89% used; 110384887 free inodes.

server2 `/home`: 19851341824 available bytes; 98.89% used; 110384887 free inodes.

server2 `/tmp`: 19851341824 available bytes; 98.89% used; 110384887 free inodes.

server2 `/var/tmp`: 19851341824 available bytes; 98.89% used; 110384887 free inodes.

server2 `/mnt/raid5`: 241924108288 available bytes; 98.33% used; 444978923 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82648920064 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82648920064 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123566469120 available bytes; 98.29% used; 225825780 free inodes.

server3 `/tmp`: 82648920064 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82648920064 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105925316608 available bytes; 94.09% used; 114347946 free inodes.

server4 `/home`: 105925316608 available bytes; 94.09% used; 114347946 free inodes.

server4 `/data`: 88802902016 available bytes; 98.77% used; 224880397 free inodes.

server4 `/tmp`: 105925316608 available bytes; 94.09% used; 114347946 free inodes.

server4 `/var/tmp`: 105925316608 available bytes; 94.09% used; 114347946 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
