# V2R cluster inventory

2026-09-26T15:01:09.025767+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318173806592 available bytes; 82.25% used; 112474033 free inodes.

server1 `/home`: 318173806592 available bytes; 82.25% used; 112474033 free inodes.

server1 `/tmp`: 318173806592 available bytes; 82.25% used; 112474033 free inodes.

server1 `/var/tmp`: 318173806592 available bytes; 82.25% used; 112474033 free inodes.

server1 `/mnt/raid5`: 655427842048 available bytes; 96.99% used; 337531875 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 43106304 available bytes; 100.00% used; 110367063 free inodes.

server2 `/home`: 43106304 available bytes; 100.00% used; 110367063 free inodes.

server2 `/tmp`: 43106304 available bytes; 100.00% used; 110367063 free inodes.

server2 `/var/tmp`: 43106304 available bytes; 100.00% used; 110367063 free inodes.

server2 `/mnt/raid5`: 623978074112 available bytes; 95.69% used; 444973652 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82737524736 available bytes; 95.38% used; 114110773 free inodes.

server3 `/home`: 82737524736 available bytes; 95.38% used; 114110773 free inodes.

server3 `/data`: 1346838003712 available bytes; 81.39% used; 225804851 free inodes.

server3 `/tmp`: 82737524736 available bytes; 95.38% used; 114110773 free inodes.

server3 `/var/tmp`: 82737524736 available bytes; 95.38% used; 114110773 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953099776 available bytes; 94.09% used; 114347839 free inodes.

server4 `/home`: 105953099776 available bytes; 94.09% used; 114347839 free inodes.

server4 `/data`: 410818768896 available bytes; 94.32% used; 224826206 free inodes.

server4 `/tmp`: 105953099776 available bytes; 94.09% used; 114347839 free inodes.

server4 `/var/tmp`: 105953099776 available bytes; 94.09% used; 114347839 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
