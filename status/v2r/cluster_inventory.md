# V2R cluster inventory

2026-09-26T09:16:23.238962+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318737117184 available bytes; 82.22% used; 112475800 free inodes.

server1 `/home`: 318737117184 available bytes; 82.22% used; 112475800 free inodes.

server1 `/tmp`: 318737117184 available bytes; 82.22% used; 112475800 free inodes.

server1 `/var/tmp`: 318737117184 available bytes; 82.22% used; 112475800 free inodes.

server1 `/mnt/raid5`: 218999046144 available bytes; 99.00% used; 337538722 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22326837248 available bytes; 98.75% used; 110403915 free inodes.

server2 `/home`: 22326837248 available bytes; 98.75% used; 110403915 free inodes.

server2 `/tmp`: 22326837248 available bytes; 98.75% used; 110403915 free inodes.

server2 `/var/tmp`: 22326837248 available bytes; 98.75% used; 110403915 free inodes.

server2 `/mnt/raid5`: 254059323392 available bytes; 98.24% used; 445023184 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661441536 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82661441536 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123661004800 available bytes; 98.29% used; 225828057 free inodes.

server3 `/tmp`: 82661441536 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82661441536 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106045960192 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106045960192 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89327800320 available bytes; 98.77% used; 224883318 free inodes.

server4 `/tmp`: 106045960192 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106045960192 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
