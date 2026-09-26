# V2R cluster inventory

2026-09-26T11:18:27.423617+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318216097792 available bytes; 82.25% used; 112474825 free inodes.

server1 `/home`: 318216097792 available bytes; 82.25% used; 112474825 free inodes.

server1 `/tmp`: 318216097792 available bytes; 82.25% used; 112474825 free inodes.

server1 `/var/tmp`: 318216097792 available bytes; 82.25% used; 112474825 free inodes.

server1 `/mnt/raid5`: 218723692544 available bytes; 99.00% used; 337538134 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19845148672 available bytes; 98.89% used; 110384879 free inodes.

server2 `/home`: 19845148672 available bytes; 98.89% used; 110384879 free inodes.

server2 `/tmp`: 19845148672 available bytes; 98.89% used; 110384879 free inodes.

server2 `/var/tmp`: 19845148672 available bytes; 98.89% used; 110384879 free inodes.

server2 `/mnt/raid5`: 241781919744 available bytes; 98.33% used; 444978649 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 82648223744 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82648223744 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123503312896 available bytes; 98.29% used; 225825703 free inodes.

server3 `/tmp`: 82648223744 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82648223744 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918275584 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105918275584 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88793812992 available bytes; 98.77% used; 224880335 free inodes.

server4 `/tmp`: 105918275584 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105918275584 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
